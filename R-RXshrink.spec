%global packname  RXshrink
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Maximum Likelihood Shrinkage via Generalized Ridge or Least Angle Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lars 

BuildRequires:    R-devel tex(latex) R-lars 

%description
Identify and display TRACEs for a specified shrinkage path and determine
the extent of shrinkage most likely, under normal distribution theory, to
produce an optimal reduction in MSE Risk in estimates of regression (beta)

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
%doc %{rlibdir}/RXshrink/doc
%doc %{rlibdir}/RXshrink/html
%doc %{rlibdir}/RXshrink/DESCRIPTION
%{rlibdir}/RXshrink/R
%{rlibdir}/RXshrink/data
%{rlibdir}/RXshrink/Meta
%{rlibdir}/RXshrink/help
%{rlibdir}/RXshrink/INDEX
%{rlibdir}/RXshrink/demo
%{rlibdir}/RXshrink/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora