%global packname  SamSPECTRAL
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Identifies cell population in flow cytometry data.

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Given a matrix of coordinates as input, SamSPECTRAL first builds the
communities to sample the data points. Then, it builds a graph and after
weighting the edges by conductance computation, the graph is passed to a
classic spectral clustering algorithm to find the spectral clusters. The
last stage of SamSPECTRAL is to combine the spectral clusters. The
resulting "connected components" estimate biological cell populations in
the data sample. For instructions on manual installation, refer to the PDF
file provided in the following documentation.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%doc %{rlibdir}/SamSPECTRAL/DESCRIPTION
%doc %{rlibdir}/SamSPECTRAL/doc
%doc %{rlibdir}/SamSPECTRAL/html
%{rlibdir}/SamSPECTRAL/INDEX
%{rlibdir}/SamSPECTRAL/help
%{rlibdir}/SamSPECTRAL/data
%{rlibdir}/SamSPECTRAL/NAMESPACE
%{rlibdir}/SamSPECTRAL/libs
%{rlibdir}/SamSPECTRAL/R
%{rlibdir}/SamSPECTRAL/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora