%global packname  startupmsg
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.7.2
Release:          1%{?dist}
Summary:          Utilities for start-up messages

Group:            Applications/Engineering 
License:          LGPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Utilities for start-up messages

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
%doc %{rlibdir}/startupmsg/NEWS
%doc %{rlibdir}/startupmsg/html
%doc %{rlibdir}/startupmsg/DESCRIPTION
%{rlibdir}/startupmsg/INDEX
%{rlibdir}/startupmsg/help
%{rlibdir}/startupmsg/TOBEDONE
%{rlibdir}/startupmsg/Meta
%{rlibdir}/startupmsg/NAMESPACE
%{rlibdir}/startupmsg/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.2-1
- initial package for Fedora