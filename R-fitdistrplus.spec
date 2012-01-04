%global packname  fitdistrplus
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2.2
Release:          1%{?dist}
Summary:          Help to fit of a parametric distribution to non-censored or censored data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Extends the fitdistr function (of the MASS package) with several functions
to help the fit of a parametric distribution to non-censored or censored
data. Censored data may contain left censored, right censored and interval
censored values, with several lower and upper bounds. In addition to
maximum likelihood estimation method the package provides moment matching,
quantile matching and maximum goodness-of-fit estimation methods
(available only for non censored data).

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
%doc %{rlibdir}/fitdistrplus/NEWS
%doc %{rlibdir}/fitdistrplus/doc
%doc %{rlibdir}/fitdistrplus/LICENCE
%doc %{rlibdir}/fitdistrplus/CITATION
%doc %{rlibdir}/fitdistrplus/html
%doc %{rlibdir}/fitdistrplus/DESCRIPTION
%{rlibdir}/fitdistrplus/gpl-3.0.txt
%{rlibdir}/fitdistrplus/NAMESPACE
%{rlibdir}/fitdistrplus/R
%{rlibdir}/fitdistrplus/help
%{rlibdir}/fitdistrplus/Meta
%{rlibdir}/fitdistrplus/data
%{rlibdir}/fitdistrplus/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2.2-1
- initial package for Fedora