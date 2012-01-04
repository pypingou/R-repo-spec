%global packname  Hotelling
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          Hotelling's T-squared test and variants

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-corpcor 

BuildRequires:    R-devel tex(latex) R-corpcor 

%description
A set of R functions and data sets which implements Hotelling's T^2 test,
and some variants of it. Functions are also included for Aitchison's
additive log ratio and centred log ratio transformations

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
%doc %{rlibdir}/Hotelling/html
%doc %{rlibdir}/Hotelling/DESCRIPTION
%{rlibdir}/Hotelling/data
%{rlibdir}/Hotelling/help
%{rlibdir}/Hotelling/Meta
%{rlibdir}/Hotelling/INDEX
%{rlibdir}/Hotelling/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora