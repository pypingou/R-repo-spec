%global packname  occugene
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.14.0
Release:          1%{?dist}
Summary:          Functions for Multinomial Occupancy Distribution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Statistical tools for building random mutagenesis libraries for
prokaryotes. The package has functions for handling the occupancy
distribution for a multinomial and for estimating the number of essential
genes in random transposon mutagenesis libraries.

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
%doc %{rlibdir}/occugene/html
%doc %{rlibdir}/occugene/DESCRIPTION
%doc %{rlibdir}/occugene/doc
%{rlibdir}/occugene/help
%{rlibdir}/occugene/INDEX
%{rlibdir}/occugene/Meta
%{rlibdir}/occugene/data
%{rlibdir}/occugene/R
%{rlibdir}/occugene/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.14.0-1
- initial package for Fedora