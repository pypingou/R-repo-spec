%global packname  ellipse
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.3.5
Release:          1%{?dist}
Summary:          Functions for drawing ellipses and ellipse-like confidence regions

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-graphics R-stats 

%description
This package contains various routines for drawing ellipses and
ellipse-like confidence regions, implementing the plots described in
Murdoch and Chow (1996), A graphical display of large correlation
matrices, The American Statistician 50, 178-180. There are also routines
implementing the profile plots described in Bates and Watts (1988),
Nonlinear Regression Analysis and its Applications.

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
%doc %{rlibdir}/ellipse/DESCRIPTION
%doc %{rlibdir}/ellipse/html
%{rlibdir}/ellipse/INDEX
%{rlibdir}/ellipse/Meta
%{rlibdir}/ellipse/R
%{rlibdir}/ellipse/NAMESPACE
%{rlibdir}/ellipse/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.5-1
- initial package for Fedora