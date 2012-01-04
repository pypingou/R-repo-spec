%global packname  doBy
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          4.4.3
Release:          1%{?dist}
Summary:          doBy - Groupwise summary statistics, general linear contrasts, LSMEANS (least-squares-means), and other utilities

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-survival R-R2HTML R-multcomp R-lme4 R-snow R-MASS 
Requires:         R-Matrix 

BuildRequires:    R-devel tex(latex) R-survival R-R2HTML R-multcomp R-lme4 R-snow R-MASS
BuildRequires:    R-Matrix 


%description
doBy contains a variety of utilities including: 1) Facilities for
groupwise computations of summary statistics and other facilities for
working with grouped data. 2) General linear contrasts and LSMEANS
(least-squares-means also known as population means), 3) Rscript2HTML for
autmatic generation of HTML file from R-script with a minimum of markup,
4) implementation of the Kenward-Roger method for estimating denominator
degrees of freedom various for tests in linear mixed models, 5) methods
for determining p-values based on parametric bootstrap in linear mixed
models 6) other utilities. doBy originally contained facilities for 'doing
something to data where data would be partitioned by some variables which
define groupings of data' - hence the name doBy.

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
%doc %{rlibdir}/doBy/html
%doc %{rlibdir}/doBy/DESCRIPTION
%doc %{rlibdir}/doBy/doc
%{rlibdir}/doBy/HTMLreport
%{rlibdir}/doBy/help
%{rlibdir}/doBy/Meta
%{rlibdir}/doBy/data
%{rlibdir}/doBy/R
%{rlibdir}/doBy/NAMESPACE
%{rlibdir}/doBy/INDEX

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 4.4.3-1
- initial package for Fedora