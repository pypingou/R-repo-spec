%global packname  data.table
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.7.2
Release:          1%{?dist}
Summary:          Extension of data.frame for fast indexing, fast ordered joins, fast assignment, fast grouping and list columns.

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Enhanced data.frame. Fast indexing, fast ordered joins, fast assignment,
fast grouping and list columns in a short and flexible syntax. i and j may
be expressions of column names directly, for faster development.  Example:
X[Y] is a fast join for large data.

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
%doc %{rlibdir}/data.table/DESCRIPTION
%doc %{rlibdir}/data.table/NEWS
%doc %{rlibdir}/data.table/doc
%doc %{rlibdir}/data.table/html
%{rlibdir}/data.table/tests
%{rlibdir}/data.table/Meta
%{rlibdir}/data.table/libs
%{rlibdir}/data.table/NAMESPACE
%{rlibdir}/data.table/R
%{rlibdir}/data.table/INDEX
%{rlibdir}/data.table/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.7.2-1
- initial package for Fedora