%global packname  alr3
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.0.5
Release:          1%{?dist}
Summary:          Data to accompany Applied Linear Regression 3rd edition

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-car 

BuildRequires:    R-devel tex(latex) R-car 

%description
This package is a companion to the textbook S. Weisberg (2005), "Applied
Linear Regression," 3rd edition, Wiley. It includes all the data sets
discussed in the book (except one), and a few functions that are tailored
to the methods discussed in the book.  As of version 2.0.0, this package
depends on the car package. Many functions formerly in alr3 have been
renamed and now reside in car. Data files have beeen lightly modified to
make some data columns row labels.

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
%doc %{rlibdir}/alr3/CITATION
%doc %{rlibdir}/alr3/DESCRIPTION
%doc %{rlibdir}/alr3/html
%doc %{rlibdir}/alr3/NEWS
%{rlibdir}/alr3/extdata
%{rlibdir}/alr3/Meta
%{rlibdir}/alr3/data
%{rlibdir}/alr3/R
%{rlibdir}/alr3/NAMESPACE
%{rlibdir}/alr3/help
%{rlibdir}/alr3/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.0.5-1
- initial package for Fedora