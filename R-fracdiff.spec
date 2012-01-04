%global packname  fracdiff
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.4.0
Release:          1%{?dist}
Summary:          Fractionally differenced ARIMA aka ARFIMA(p,d,q) models

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.4-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Maximum likelihood estimation of the parameters of a fractionally
differenced ARIMA(p,d,q) model (Haslett and Raftery, Appl.Statistics,

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
%doc %{rlibdir}/fracdiff/html
%doc %{rlibdir}/fracdiff/DESCRIPTION
%{rlibdir}/fracdiff/help
%{rlibdir}/fracdiff/INDEX
%{rlibdir}/fracdiff/Meta
%{rlibdir}/fracdiff/libs
%{rlibdir}/fracdiff/R
%{rlibdir}/fracdiff/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.4.0-1
- initial package for Fedora