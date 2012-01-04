%global packname  wordnet
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.8
Release:          1%{?dist}
Summary:          WordNet Interface

Group:            Applications/Engineering 
License:          MIT
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-rJava 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-rJava 


%description
An interface to WordNet using the Jawbone Java API to WordNet. WordNet is
an on-line lexical reference system developed by the Cognitive Science
Laboratory at Princeton University. Its design is inspired by current
psycholinguistic theories of human lexical memory. English nouns, verbs,
adjectives and adverbs are organized into synonym sets, each representing
one underlying lexical concept. Different relations link the synonym sets.

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
%doc %{rlibdir}/wordnet/CITATION
%doc %{rlibdir}/wordnet/DESCRIPTION
%doc %{rlibdir}/wordnet/doc
%doc %{rlibdir}/wordnet/html
%{rlibdir}/wordnet/help
%{rlibdir}/wordnet/Meta
%{rlibdir}/wordnet/R
%{rlibdir}/wordnet/INDEX
%{rlibdir}/wordnet/java
%{rlibdir}/wordnet/NAMESPACE

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.8-1
- initial package for Fedora