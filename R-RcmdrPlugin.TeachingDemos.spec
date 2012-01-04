%global packname  RcmdrPlugin.TeachingDemos
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.5
Release:          1%{?dist}
Summary:          Rcmdr Teaching Demos Plug-In

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-tcltk R-TeachingDemos 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-tcltk R-TeachingDemos 

%description
This package provides an Rcmdr "plug-in" based on the TeachingDemos
package, and is primarily for illustrative purposes.

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
%doc %{rlibdir}/RcmdrPlugin.TeachingDemos/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.TeachingDemos/html
%{rlibdir}/RcmdrPlugin.TeachingDemos/help
%{rlibdir}/RcmdrPlugin.TeachingDemos/Meta
%{rlibdir}/RcmdrPlugin.TeachingDemos/CHANGES
%{rlibdir}/RcmdrPlugin.TeachingDemos/NAMESPACE
%{rlibdir}/RcmdrPlugin.TeachingDemos/etc
%{rlibdir}/RcmdrPlugin.TeachingDemos/R
%{rlibdir}/RcmdrPlugin.TeachingDemos/INDEX

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.5-1
- initial package for Fedora