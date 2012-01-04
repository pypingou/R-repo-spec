%global packname  prefmod
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.8.27
Release:          1%{?dist}
Summary:          Utilities to fit paired comparison models for preferences

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.8-27.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-stats R-gnm R-colorspace 


BuildRequires:    R-devel tex(latex) R-stats R-gnm R-colorspace



%description
Generates design matrix for analysing real paired comparisons and derived
paired comparison data (Likert type items / ratings or rankings) using a
loglinear approach.  Fits loglinear Bradley-Terry model (LLBT) exploting
an eliminate feature.  Computes pattern models for paired comparisons,
rankings, and ratings.  Some treatment of missing values (MCAR and MNAR).
Fits latent class (mixture) models for paired comparison, rating and
ranking patterns using a nonparametric ML approach.

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
%doc %{rlibdir}/prefmod/DESCRIPTION
%doc %{rlibdir}/prefmod/html
%{rlibdir}/prefmod/INDEX
%{rlibdir}/prefmod/NAMESPACE
%{rlibdir}/prefmod/help
%{rlibdir}/prefmod/Meta
%{rlibdir}/prefmod/R
%{rlibdir}/prefmod/data
%{rlibdir}/prefmod/libs

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.8.27-1
- initial package for Fedora