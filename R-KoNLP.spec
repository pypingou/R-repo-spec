%global packname  KoNLP
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.7.4
Release:          1%{?dist}
Summary:          Korean NLP Package

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-7.4.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) R-rJava 

%description
Korean Language Processing, An interface to Hannanum korean
analyzer.(http://semanticweb.kaist.ac.kr/home/index.php/HanNanum), An
interface to Korean Lucene
analyzer.(http://sourceforge.net/projects/lucenekorean/), some functions

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
%doc %{rlibdir}/KoNLP/DESCRIPTION
%doc %{rlibdir}/KoNLP/html
%{rlibdir}/KoNLP/help
%{rlibdir}/KoNLP/dics
%{rlibdir}/KoNLP/NAMESPACE
%{rlibdir}/KoNLP/Meta
%{rlibdir}/KoNLP/INDEX
%{rlibdir}/KoNLP/java
%{rlibdir}/KoNLP/R

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.7.4-1
- initial package for Fedora