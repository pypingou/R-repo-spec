%global packname  interval
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1.2
Release:          1%{?dist}
Summary:          Weighted Logrank Tests and NPMLE for interval censored data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-survival R-perm R-Icens R-MLEcens 

BuildRequires:    R-devel tex(latex) R-stats R-survival R-perm R-Icens R-MLEcens 

%description
Functions to fit nonparametric survival curves, plot them, and perform
logrank or Wilcoxon type tests.

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
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1.2-1
- initial package for Fedora