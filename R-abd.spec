%global packname  abd
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.22
Release:          1%{?dist}
Summary:          The Analysis of Biological Data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-22.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-nlme R-lattice R-grid 

BuildRequires:    R-devel tex(latex) R-nlme R-lattice R-grid 

%description
The abd package contains data sets and sample code for The Analysis of
Biological Data by Michael Whitlock and Dolph Schluter (2009; Roberts &
Company Publishers).

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
%doc %{rlibdir}/abd/DESCRIPTION
%doc %{rlibdir}/abd/html
%doc %{rlibdir}/abd/NEWS
%{rlibdir}/abd/README
%{rlibdir}/abd/Meta
%{rlibdir}/abd/NAMESPACE
%{rlibdir}/abd/demo
%{rlibdir}/abd/R
%{rlibdir}/abd/THANKS
%{rlibdir}/abd/INDEX
%{rlibdir}/abd/data
%{rlibdir}/abd/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.22-1
- initial package for Fedora