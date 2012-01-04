%global packname  robust
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.11
Release:          1%{?dist}
Summary:          Insightful Robust Library

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-11.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS R-lattice R-robustbase R-rrcov R-stats 

BuildRequires:    R-devel tex(latex) R-MASS R-lattice R-robustbase R-rrcov R-stats 

%description
A package of robust methods.

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
%changelog
* Thu Dec 01 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.11-1
- initial package for Fedora