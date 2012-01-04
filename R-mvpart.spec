%global packname  mvpart
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Multivariate partitioning

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Multivariate regression trees

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
%doc %{rlibdir}/mvpart/html
%doc %{rlibdir}/mvpart/DESCRIPTION
%{rlibdir}/mvpart/NAMESPACE
%{rlibdir}/mvpart/Meta
%{rlibdir}/mvpart/LICENSE
%{rlibdir}/mvpart/R
%{rlibdir}/mvpart/INDEX
%{rlibdir}/mvpart/help
%{rlibdir}/mvpart/libs
%{rlibdir}/mvpart/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora