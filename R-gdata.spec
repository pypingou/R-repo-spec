%global packname  gdata
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.8.2
Release:          1%{?dist}
Summary:          Various R programming tools for data manipulation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-gtools 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-gtools 


%description
Various R programming tools for data manipulation

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
%doc %{rlibdir}/gdata/NEWS
%doc %{rlibdir}/gdata/html
%doc %{rlibdir}/gdata/DESCRIPTION
%doc %{rlibdir}/gdata/doc
%{rlibdir}/gdata/INDEX
%{rlibdir}/gdata/Meta
%{rlibdir}/gdata/unitTests
%{rlibdir}/gdata/ChangeLog
%{rlibdir}/gdata/xls
%{rlibdir}/gdata/R
%{rlibdir}/gdata/data
%{rlibdir}/gdata/perl
RPM build errors:
%{rlibdir}/gdata/bin
%{rlibdir}/gdata/help
%{rlibdir}/gdata/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.8.2-1
- initial package for Fedora