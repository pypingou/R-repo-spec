%global packname  soil.spec
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.4
Release:          1%{?dist}
Summary:          Soil spectral data exploration and regression functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package combines existing R functions with new code for soil spectral
analysis. The result is an easy to use tool for (i) importing of
spc-files, (ii) principal component analysis, (iii) sample selection using
the Kennard-Stone algorithm, (iv) spectral transformation and (v)
comparison of regression methods.

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
%doc %{rlibdir}/soil.spec/DESCRIPTION
%doc %{rlibdir}/soil.spec/html
%{rlibdir}/soil.spec/INDEX
%{rlibdir}/soil.spec/help
%{rlibdir}/soil.spec/R
%{rlibdir}/soil.spec/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4-1
- initial package for Fedora