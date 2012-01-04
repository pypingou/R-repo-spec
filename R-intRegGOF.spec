%global packname  intRegGOF
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.85.1
Release:          1%{?dist}
Summary:          Integrated Regression Goodness of Fit

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.85-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Performs Goodness of Fit for regression models using

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
%doc %{rlibdir}/intRegGOF/html
%doc %{rlibdir}/intRegGOF/DESCRIPTION
%{rlibdir}/intRegGOF/R
%{rlibdir}/intRegGOF/Meta
%{rlibdir}/intRegGOF/help
%{rlibdir}/intRegGOF/INDEX
%{rlibdir}/intRegGOF/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.85.1-1
- initial package for Fedora