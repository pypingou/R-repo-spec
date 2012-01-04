%global packname  ordPens
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Selection and/or Smoothing of Ordinal Predictors

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-grplasso 

BuildRequires:    R-devel tex(latex) R-grplasso 

%description
Selection and/or smoothing of ordinally scaled independent variables using
a Group Lasso or generalized Ridge penalty

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
%doc %{rlibdir}/ordPens/DESCRIPTION
%doc %{rlibdir}/ordPens/html
%{rlibdir}/ordPens/Meta
%{rlibdir}/ordPens/INDEX
%{rlibdir}/ordPens/R
%{rlibdir}/ordPens/help
%{rlibdir}/ordPens/data

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora