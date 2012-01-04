%global packname  RobAStBase
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.1
Release:          1%{?dist}
Summary:          Robust Asymptotic Statistics

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-distr R-distrEx R-distrMod R-RandVar 

BuildRequires:    R-devel tex(latex) R-methods R-distr R-distrEx R-distrMod R-RandVar 

%description
Base S4-classes and functions for robust asymptotic statistics.

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.1-1
- initial package for Fedora