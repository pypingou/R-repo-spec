%global packname  RcmdrPlugin.survival
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          R Commander Plug-in for the survival Package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-tcltk R-survival R-date 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-tcltk R-survival R-date 

%description
This package provides an R Commander plug-in for the survival package,
with dialogs for Cox models, parametric survival regression models,
estimation of survival curves, and testing for differences in survival
curves, along with data-management facilities and a variety of tests,
diagnostics and graphs.

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
%doc %{rlibdir}/RcmdrPlugin.survival/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.survival/html
%{rlibdir}/RcmdrPlugin.survival/CHANGES
%{rlibdir}/RcmdrPlugin.survival/help
%{rlibdir}/RcmdrPlugin.survival/INDEX
%{rlibdir}/RcmdrPlugin.survival/Meta
%{rlibdir}/RcmdrPlugin.survival/po
%{rlibdir}/RcmdrPlugin.survival/R
%{rlibdir}/RcmdrPlugin.survival/data
%{rlibdir}/RcmdrPlugin.survival/etc

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora