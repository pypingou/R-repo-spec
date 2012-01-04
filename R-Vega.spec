%global packname  Vega
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.0
Release:          1%{?dist}
Summary:          An R package for copy number data segmentation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Vega (Variational Estimator for Genomic Aberrations) is an algorithm that
adapts a very popular variational model (Mumford and Shah) used in image
segmentation so that chromosomal aberrant regions can be efficiently

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
%doc %{rlibdir}/Vega/doc
%doc %{rlibdir}/Vega/DESCRIPTION
%doc %{rlibdir}/Vega/html
%{rlibdir}/Vega/help
%{rlibdir}/Vega/INDEX
%{rlibdir}/Vega/Meta
%{rlibdir}/Vega/NAMESPACE
%{rlibdir}/Vega/libs
%{rlibdir}/Vega/R
%{rlibdir}/Vega/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.0-1
- initial package for Fedora