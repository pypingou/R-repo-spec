%global packname  gregmisc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1.2
Release:          1%{?dist}
Summary:          Greg's Miscellaneous Functions

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-gdata R-gmodels R-gplots R-gtools 


BuildRequires:    R-devel tex(latex) R-gdata R-gmodels R-gplots R-gtools



%description
The former gregmisc bundle is a repository for a variety of useful
functions.  The gregmisc package was recently split into a set of more
focused packages: gdata, gmodels, gplots, gtools. The purpose of this
'new' gregmisc is to provide an easy way to access the original combined
functionality.  To this end, it simply depends on all of the new packages
so that these will installed/loaded when this package is installed/loaded.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.2-1
- initial package for Fedora