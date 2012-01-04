%global packname  mlogit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          multinomial logit model

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Formula R-statmod R-lmtest R-maxLik R-zoo R-MASS 


BuildRequires:    R-devel tex(latex) R-Formula R-statmod R-lmtest R-maxLik R-zoo R-MASS



%description
Estimation of the multinomial logit model

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
%doc %{rlibdir}/mlogit/DESCRIPTION
%doc %{rlibdir}/mlogit/doc
%doc %{rlibdir}/mlogit/html
%{rlibdir}/mlogit/INDEX
%{rlibdir}/mlogit/help
%{rlibdir}/mlogit/Meta
%{rlibdir}/mlogit/data
%{rlibdir}/mlogit/NAMESPACE
%{rlibdir}/mlogit/R

%changelog
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora