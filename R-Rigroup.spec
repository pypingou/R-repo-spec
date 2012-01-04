%global packname  Rigroup
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.83.0
Release:          1%{?dist}
Summary:          Rigroup: Provides small integer group functions

Group:            Applications/Engineering 
License:          GPL or LGPL by your choice
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A package to provide small integer group functions

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
%doc %{rlibdir}/Rigroup/doc
%doc %{rlibdir}/Rigroup/html
%doc %{rlibdir}/Rigroup/DESCRIPTION
%{rlibdir}/Rigroup/NAMESPACE
%{rlibdir}/Rigroup/Meta
%{rlibdir}/Rigroup/libs
%{rlibdir}/Rigroup/help
%{rlibdir}/Rigroup/R
%{rlibdir}/Rigroup/po
%{rlibdir}/Rigroup/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.83.0-1
- initial package for Fedora