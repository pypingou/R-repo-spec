%global packname  mapReduce
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2.3
Release:          1%{?dist}
Summary:          mapReduce - flexible mapReduce algorithm for parallel computation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
mapReduce is an algorithm provides a simple framework for parallel
computations.  This implementation provides (a) a pure R implementation
(b) a syntax following the mapReduce paper and (c) flexible and
parallelizable back end.

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
%doc %{rlibdir}/mapReduce/DESCRIPTION
%doc %{rlibdir}/mapReduce/html
%{rlibdir}/mapReduce/NAMESPACE
%{rlibdir}/mapReduce/R
%{rlibdir}/mapReduce/INDEX
%{rlibdir}/mapReduce/help
%{rlibdir}/mapReduce/Meta
%{rlibdir}/mapReduce/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.3-1
- initial package for Fedora