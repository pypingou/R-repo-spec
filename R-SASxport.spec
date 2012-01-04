%global packname  SASxport
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.4
Release:          1%{?dist}
Summary:          Read and Write SAS XPORT Files

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-chron 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-chron 


%description
This package provides functions for reading, listing the contents of, and
writing SAS xport format files. The functions support reading and writing
of either individual data frames or sets of data frames.  Further, a
mechanism has been provided for customizing how variables of different
data types are stored.

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
%doc %{rlibdir}/SASxport/NEWS
%doc %{rlibdir}/SASxport/html
%doc %{rlibdir}/SASxport/DESCRIPTION
%{rlibdir}/SASxport/NAMESPACE
%{rlibdir}/SASxport/ChangeLog
%{rlibdir}/SASxport/libs
%{rlibdir}/SASxport/Meta
%{rlibdir}/SASxport/data
%{rlibdir}/SASxport/INDEX
%{rlibdir}/SASxport/R
%{rlibdir}/SASxport/help

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.4-1
- initial package for Fedora