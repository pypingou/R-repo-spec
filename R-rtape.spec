%global packname  rtape
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Manage and manipulate large collections of R objects stored as tape-like files

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Storing huge data in RData format causes problems because of the nessesity
to load the whole file to the memory in order to access and manipulate
objects inside such file; rtape is a simple solution to this problem. The
package contains serveral wrappers of R built-in serialize/unserialize
mechanism allowing user to quickly append objects to a tape-like file and
later iterate over them requiring only one copy of each stored object to
reside in memory a time.

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
%doc %{rlibdir}/rtape/html
%doc %{rlibdir}/rtape/DESCRIPTION
%{rlibdir}/rtape/NAMESPACE
%{rlibdir}/rtape/R
%{rlibdir}/rtape/INDEX
%{rlibdir}/rtape/help
%{rlibdir}/rtape/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora