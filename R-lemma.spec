%global packname  lemma
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.1
Release:          1%{?dist}
Summary:          Laplace approximated EM Microarray Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
LEMMA is used to detect "nonnull genes" - genes for which the average
response in treatment group 1 is significantly different from the average
response in group 2, in normalized microarray data. LEMMA is an
implementation of an approximate EM algorithm to estimate the parameters
in the assumed linear model in Bar, Booth, Schifano, Wells (2009).

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
%doc %{rlibdir}/lemma/DESCRIPTION
%doc %{rlibdir}/lemma/html
%{rlibdir}/lemma/Meta
%{rlibdir}/lemma/help
%{rlibdir}/lemma/INDEX
%{rlibdir}/lemma/data
%{rlibdir}/lemma/R
%{rlibdir}/lemma/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.1-1
- initial package for Fedora