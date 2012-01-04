%global packname  hda
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1.17
Release:          1%{?dist}
Summary:          Heteroscedastic Discriminant Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-17.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core


Requires:         R-e1071 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-e1071 


%description
Functions to perform dimensionality reduction for classification if the
covariance matrices of the classes are unequal.

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
%doc %{rlibdir}/hda/html
%doc %{rlibdir}/hda/DESCRIPTION
%{rlibdir}/hda/INDEX
%{rlibdir}/hda/help
%{rlibdir}/hda/Meta
%{rlibdir}/hda/R
%{rlibdir}/hda/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.17-1
- initial package for Fedora