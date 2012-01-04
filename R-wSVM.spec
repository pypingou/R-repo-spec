%global packname  wSVM
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Weighted SVM with boosting algorithm for improving accuracy

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-MASS R-quadprog 

BuildRequires:    R-devel tex(latex) R-MASS R-quadprog 

%description
We propose weighted SVM methods with penalization form. By adding weights
to loss term, we can build up weighted SVM easily and examine
classification algorithm properties under weighted SVM. Through comparing
each of test error rates, we conclude that our Weighted SVM with boosting
has predominant properties than the standard SVM have, as a whole.

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
%doc %{rlibdir}/wSVM/LICENCE
%doc %{rlibdir}/wSVM/html
%doc %{rlibdir}/wSVM/DESCRIPTION
%{rlibdir}/wSVM/data
%{rlibdir}/wSVM/help
%{rlibdir}/wSVM/Meta
%{rlibdir}/wSVM/INDEX
%{rlibdir}/wSVM/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora