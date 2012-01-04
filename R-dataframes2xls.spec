%global packname  dataframes2xls
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.5
Release:          1%{?dist}
Summary:          dataframes2xls writes data frames to xls files

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
dataframes2xls writes data frames to xls files. It supports multiple
sheets and basic formatting.

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
%doc %{rlibdir}/dataframes2xls/html
%doc %{rlibdir}/dataframes2xls/DESCRIPTION
%doc %{rlibdir}/dataframes2xls/doc
%{rlibdir}/dataframes2xls/LICENSE
%{rlibdir}/dataframes2xls/NAMESPACE
%{rlibdir}/dataframes2xls/Meta
%{rlibdir}/dataframes2xls/python
%{rlibdir}/dataframes2xls/INDEX
RPM build errors:
%{rlibdir}/dataframes2xls/help
%{rlibdir}/dataframes2xls/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.5-1
- initial package for Fedora