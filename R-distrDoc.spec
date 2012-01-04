%global packname  distrDoc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.3.1
Release:          1%{?dist}
Summary:          Documentation for packages distr, distrEx, distrSim, distrTEst, distrTeach, distrMod, and distrEllipse

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tools R-startupmsg R-distr R-distrEx R-distrSim R-distrTEst R-distrTeach R-RandVar R-distrMod R-MASS R-methods 

BuildRequires:    R-devel tex(latex) R-tools R-startupmsg R-distr R-distrEx R-distrSim R-distrTEst R-distrTeach R-RandVar R-distrMod R-MASS R-methods 

%description
provides documentation in form of a common vignette to packages distr,
distrEx, distrMod, distrSim, distrTEst, distrTeach, and distrEllipse

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
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.3.1-1
- initial package for Fedora