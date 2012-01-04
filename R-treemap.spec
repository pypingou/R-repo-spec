%global packname  treemap
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.10
Release:          1%{?dist}
Summary:          Treemap visualization

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grid R-RColorBrewer R-plyr 


BuildRequires:    R-devel tex(latex) R-grid R-RColorBrewer R-plyr



%description
With this package, different kind of treemaps can be generated such as
comparison treemaps and density treemaps. Further, it is possible to show
small multiples.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.10-1
- initial package for Fedora