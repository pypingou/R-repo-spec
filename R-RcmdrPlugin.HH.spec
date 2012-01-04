%global packname  RcmdrPlugin.HH
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.29
Release:          1%{?dist}
Summary:          Rcmdr support for the HH package

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-29.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-HH R-car R-multcomp R-leaps R-lattice R-grid R-grDevices 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-HH R-car R-multcomp R-leaps R-lattice R-grid R-grDevices 

%description
Rcmdr menu support for many of the functions in the HH package.  The focus
is on menu items for functions we use in our introductory courses.

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
%doc %{rlibdir}/RcmdrPlugin.HH/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.HH/html
%{rlibdir}/RcmdrPlugin.HH/etc
%{rlibdir}/RcmdrPlugin.HH/INDEX
%{rlibdir}/RcmdrPlugin.HH/NAMESPACE
%{rlibdir}/RcmdrPlugin.HH/R
%{rlibdir}/RcmdrPlugin.HH/help
%{rlibdir}/RcmdrPlugin.HH/Meta

%changelog
* Fri Dec 02 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.29-1
- initial package for Fedora