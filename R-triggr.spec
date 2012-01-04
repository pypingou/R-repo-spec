%global packname  triggr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Fast, simple RPC controller for R

Group:            Applications/Engineering 
License:          file LICENCE | GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Triggr launches a server that gathers RNRN-terminated text messages,
executes arbitrary R function on them and sends back the results in the
same format. Communication is event-based and delegated to a septate
thread making triggr an efficient solution for high-load tasks.

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
%doc %{rlibdir}/triggr/DESCRIPTION
%doc %{rlibdir}/triggr/LICENCE
%doc %{rlibdir}/triggr/html
%{rlibdir}/triggr/INDEX
%{rlibdir}/triggr/R
%{rlibdir}/triggr/help
%{rlibdir}/triggr/NAMESPACE
%{rlibdir}/triggr/Meta
%{rlibdir}/triggr/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora