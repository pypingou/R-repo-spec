%global packname  lda.cv
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.2
Release:          1%{?dist}
Summary:          Cross-validation for linear discriminate analysis

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tcltk R-MASS 

BuildRequires:    R-devel tex(latex) R-tcltk R-MASS 

%description
This is the gui interface to calculate cross-validation of the principle
component and discriminate analysis

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
%doc %{rlibdir}/lda.cv/DESCRIPTION
%doc %{rlibdir}/lda.cv/html
%{rlibdir}/lda.cv/NAMESPACE
%{rlibdir}/lda.cv/R
%{rlibdir}/lda.cv/INDEX
%{rlibdir}/lda.cv/Meta
%{rlibdir}/lda.cv/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.2-1
- initial package for Fedora