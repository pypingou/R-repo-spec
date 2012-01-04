%global packname  hexbin
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.28.0
Release:          1%{?dist}
Summary:          Hexagonal Binning Routines

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-grid R-lattice 

BuildRequires:    R-devel tex(latex) R-methods R-grid R-lattice 

%description
Binning and plotting functions for hexagonal bins. Now uses and relies on
grid graphics and formal (S4) classes and methods.

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
%doc %{rlibdir}/hexbin/DESCRIPTION
%doc %{rlibdir}/hexbin/doc
%doc %{rlibdir}/hexbin/html
%{rlibdir}/hexbin/libs
%{rlibdir}/hexbin/INDEX
%{rlibdir}/hexbin/help
%{rlibdir}/hexbin/Meta
%{rlibdir}/hexbin/data
%{rlibdir}/hexbin/NAMESPACE
%{rlibdir}/hexbin/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.28.0-1
- initial package for Fedora