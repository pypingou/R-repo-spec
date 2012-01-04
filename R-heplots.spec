%global packname  heplots
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.10
Release:          1%{?dist}
Summary:          Visualizing Tests in Multivariate Linear Models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-10.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-car R-graphics R-stats 

BuildRequires:    R-devel tex(latex) R-car R-graphics R-stats 

%description
Provides HE plot functions for visualizing hypothesis tests in
multivariate linear models. They represents sums-of-squares-and-products
matrices for linear hypotheses and for error using ellipses (in two
dimensions) and ellipsoids (in three dimensions).

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
%doc %{rlibdir}/heplots/html
%doc %{rlibdir}/heplots/doc
%doc %{rlibdir}/heplots/NEWS
%doc %{rlibdir}/heplots/CITATION
%doc %{rlibdir}/heplots/DESCRIPTION
%{rlibdir}/heplots/demo
%{rlibdir}/heplots/Meta
%{rlibdir}/heplots/INDEX
%{rlibdir}/heplots/NAMESPACE
%{rlibdir}/heplots/help
%{rlibdir}/heplots/data
%{rlibdir}/heplots/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.10-1
- initial package for Fedora