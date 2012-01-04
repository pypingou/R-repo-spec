%global packname  PKtools
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5.0
Release:          1%{?dist}
Summary:          unified computational interfaces for pop PK

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.5-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-lattice R-nlme R-R2HTML R-xtable 

BuildRequires:    R-devel tex(latex) R-methods R-lattice R-nlme R-R2HTML R-xtable 

%description
computations for WinBUGS, NONMEM V, NLME

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
%doc %{rlibdir}/PKtools/doc
%doc %{rlibdir}/PKtools/html
%doc %{rlibdir}/PKtools/DESCRIPTION
%{rlibdir}/PKtools/nonmemAdd
%{rlibdir}/PKtools/help
%{rlibdir}/PKtools/bugsAdd
%{rlibdir}/PKtools/NAMESPACE
%{rlibdir}/PKtools/Meta
%{rlibdir}/PKtools/INDEX
%{rlibdir}/PKtools/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5.0-1
- initial package for Fedora