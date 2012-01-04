%global packname  SVMMaj
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          SVMMaj algorithm

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-kernlab 

BuildRequires:    R-devel tex(latex) R-kernlab 

%description
Implements the SVM-Maj algorithm to train data with Support Vector
Machine, this algorithm uses two efficient updates, one for linear kernel
and one for the nonlinear kernel.

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
%doc %{rlibdir}/SVMMaj/DESCRIPTION
%doc %{rlibdir}/SVMMaj/html
%{rlibdir}/SVMMaj/help
%{rlibdir}/SVMMaj/Meta
%{rlibdir}/SVMMaj/data
%{rlibdir}/SVMMaj/R
%{rlibdir}/SVMMaj/NAMESPACE
%{rlibdir}/SVMMaj/INDEX

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora