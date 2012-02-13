%global packname  tis
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.18
Release:          1%{dist}
Summary:          Time Indexes and Time Indexed Series

Group:            Applications/Engineering 
License:          Unlimited
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions and S3 classes for time indexes and time indexed series, which
are compatible with FAME frequencies.

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
%doc %{rlibdir}/tis/DESCRIPTION
%doc %{rlibdir}/tis/html
%doc %{rlibdir}/tis/NEWS
%{rlibdir}/tis/help
%{rlibdir}/tis/R
%{rlibdir}/tis/INDEX
%{rlibdir}/tis/NAMESPACE
%{rlibdir}/tis/Meta
%{rlibdir}/tis/libs

%changelog
* Sun Feb 12 2012 Pierre-Yves Chibon <pingou@pingoured.fr> 1.18-1
- Update to version 1.18

* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.17-1
- initial package for Fedora