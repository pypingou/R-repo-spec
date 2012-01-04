%global packname  moc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.5.1
Release:          1%{?dist}
Summary:          GENERAL NONLINEAR MIXTURES OF CURVES

Group:            Applications/Engineering 
License:          GPL (version 2 or later, see the included file GPL)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Fits a variety of mixtures models for multivariate observations with
user-defined distributions and profiles.

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
%doc %{rlibdir}/moc/html
%doc %{rlibdir}/moc/DESCRIPTION
%{rlibdir}/moc/Sweave
%{rlibdir}/moc/Examples
%{rlibdir}/moc/libs
%{rlibdir}/moc/GPL
%{rlibdir}/moc/Meta
%{rlibdir}/moc/GUI
%{rlibdir}/moc/NAMESPACE
%{rlibdir}/moc/R
%{rlibdir}/moc/Utils
%{rlibdir}/moc/Changes
%{rlibdir}/moc/help
%{rlibdir}/moc/data
%{rlibdir}/moc/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5.1-1
- initial package for Fedora