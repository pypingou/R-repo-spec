%global packname  mvbutils
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.5.101
Release:          1%{?dist}
Summary:          Workspace organization, code and documentation editing, package prep and editing, etc.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-utils R-tools R-stats 

BuildRequires:    R-devel tex(latex) R-utils R-tools R-stats 

%description
Hierarchical workspace tree, code editing and backup, easy package prep,
editing of packages while loaded, per-object lazy-loading, easy
documentation, macro functions, and miscellaneous utilities. Needed by
debug package.

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
%doc %{rlibdir}/mvbutils/DESCRIPTION
%doc %{rlibdir}/mvbutils/html
%{rlibdir}/mvbutils/demostuff
%{rlibdir}/mvbutils/NAMESPACE
%{rlibdir}/mvbutils/INDEX
%{rlibdir}/mvbutils/R
%{rlibdir}/mvbutils/help
%{rlibdir}/mvbutils/Meta
%{rlibdir}/mvbutils/demo
%{rlibdir}/mvbutils/changes.txt

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.5.101-1
- initial package for Fedora