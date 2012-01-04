%global packname  equivalence
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.5.6
Release:          1%{?dist}
Summary:          Provides tests and graphics for assessing tests of equivalence

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lattice R-boot R-grid 

BuildRequires:    R-devel tex(latex) R-lattice R-boot R-grid 

%description
This package provides some statistical tests and graphics for assessing
tests of equivalence.  Such tests have similarity as the alternative
hypothesis instead of the null.  Sample datasets are included.

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
%doc %{rlibdir}/equivalence/DESCRIPTION
%doc %{rlibdir}/equivalence/html
%{rlibdir}/equivalence/R
%{rlibdir}/equivalence/Meta
%{rlibdir}/equivalence/INDEX
%{rlibdir}/equivalence/data
%{rlibdir}/equivalence/NAMESPACE
%{rlibdir}/equivalence/libs
%{rlibdir}/equivalence/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.5.6-1
- initial package for Fedora