%global packname  date
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.31
Release:          1%{?dist}
Summary:          Functions for handling dates

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-31.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions for handling dates.

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
%doc %{rlibdir}/date/CITATION
%doc %{rlibdir}/date/html
%doc %{rlibdir}/date/DESCRIPTION
%{rlibdir}/date/Meta
%{rlibdir}/date/NAMESPACE
%{rlibdir}/date/libs
%{rlibdir}/date/R
%{rlibdir}/date/help
%{rlibdir}/date/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.31-1
- initial package for Fedora