%global packname  Lmoments
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.4
Release:          1%{?dist}
Summary:          L-moments and quantile mixtures

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The Lmoments package contains functions to estimate L-moments and trimmed
L-moments from the data. The package also contains functions to estimate
the parameters of the normal polynomial quantile mixture and the Cauchy
polynomial quantile mixture from L-moments and trimmed L-moments.

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
%doc %{rlibdir}/Lmoments/DESCRIPTION
%doc %{rlibdir}/Lmoments/CITATION
%doc %{rlibdir}/Lmoments/News
%doc %{rlibdir}/Lmoments/html
%{rlibdir}/Lmoments/Meta
%{rlibdir}/Lmoments/INDEX
%{rlibdir}/Lmoments/R
%{rlibdir}/Lmoments/NAMESPACE
%{rlibdir}/Lmoments/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.4-1
- initial package for Fedora