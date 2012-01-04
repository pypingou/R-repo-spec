%global packname  samplingbook
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Survey Sampling Procedures

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-pps R-sampling R-sampfling R-survey 


BuildRequires:    R-devel tex(latex) R-pps R-sampling R-sampfling R-survey



%description
Sampling procedures from the book 'Stichproben. Methoden und praktische
Umsetzung mit R' by Goeran Kauermann and Helmut Kuechenhoff (2010)

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
%doc %{rlibdir}/samplingbook/html
%doc %{rlibdir}/samplingbook/DESCRIPTION
%{rlibdir}/samplingbook/NAMESPACE
%{rlibdir}/samplingbook/help
%{rlibdir}/samplingbook/Meta
%{rlibdir}/samplingbook/INDEX
%{rlibdir}/samplingbook/data
%{rlibdir}/samplingbook/R

%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora