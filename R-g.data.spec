%global packname  g.data
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0
Release:          1%{?dist}
Summary:          Delayed-Data Packages

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Create and maintain delayed-data packages (DDP's).  Data stored in a DDP
are available on demand, but do not take up memory until requested. You
attach a DDP with g.data.attach(), then read from it and assign to it in a
manner similar to S-Plus, except that you must run g.data.save() to
actually commit to disk.

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
%doc %{rlibdir}/g.data/DESCRIPTION
%doc %{rlibdir}/g.data/html
%{rlibdir}/g.data/NAMESPACE
%{rlibdir}/g.data/help
%{rlibdir}/g.data/R
%{rlibdir}/g.data/Meta
%{rlibdir}/g.data/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0-1
- initial package for Fedora