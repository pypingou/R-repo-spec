%global packname  openNLP
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.0.8
Release:          1%{?dist}
Summary:          openNLP Interface

Group:            Applications/Engineering 
License:          LGPL-2.1
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)


Requires:         R-methods R-rJava R-tm 

BuildRequires:    R-devel tex(latex) 
BuildRequires:    R-methods R-rJava R-tm 


%description
An interface to openNLP (http://opennlp.sourceforge.net/), a collection of
natural language processing tools including a sentence detector,
tokenizer, pos-tagger, shallow and full syntactic parser, and named-entity
detector, using the Maxent Java package for training and using maximum
entropy models.

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
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.8-1
- initial package for Fedora